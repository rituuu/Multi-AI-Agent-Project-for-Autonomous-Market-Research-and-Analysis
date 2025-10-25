import subprocess
import threading
import time
from dotenv import load_dotenv
from common.logger import get_logger
from common.custom_exception import CustomException
import gradio as gr
from langchain.schema import HumanMessage

# Import your agents (make sure these are defined in your app)
from Multi_Agents.MultiAgents import research_agent, use_case_agent, resource_agent
from Multi_Agents.MultiAgents import save_resources_to_file

logger = get_logger(__name__)
load_dotenv()


def run_backend():
    try:
        logger.info("Starting backend service...")
        subprocess.run(
            ["uvicorn", "app.backend.fastapi_app:app", "--host", "0.0.0.0", "--port", "8001", "--reload"], check=True)
    except CustomException as e:
        logger.error("Problem with backend service")
        raise CustomException("Failed to start backend", e)


def run_frontend():
    try:
        logger.info("Starting frontend (Gradio UI)...")

        # Define Gradio Interface
        with gr.Blocks() as demo:
            gr.Markdown("# Multi-Agent System for AI-Powered Market Research, Use Case Generation, and Resource Collection")
            query = gr.Textbox(label="Enter Industry or Company Query")
            output = gr.Markdown()
            submit_button = gr.Button("Generate Insights")

            def gradio_interface_with_progress(query):
                import time
                progress_log = ""  # Accumulate all outputs
                try:
                    # Step 1: Research the Industry or the Company
                    yield "Step 1: Researching the Industry or the Company..."
                    research_messages = [HumanMessage(content=query)]
                    research_state = {"messages": research_messages}
                    research_result = research_agent.graph.invoke(research_state)
                    research_content = research_result["messages"][-1].content
                    progress_log += f"### Research Output:\n{research_content}\n\n"
                    time.sleep(1)

                    # Step 2: Generate Use Cases
                    yield "Step 2: Generating Use Cases..."
                    use_case_messages = [HumanMessage(content=f"Input Research: {research_content}")]
                    use_case_state = {"messages": use_case_messages}
                    use_case_result = use_case_agent.graph.invoke(use_case_state)
                    use_case_content = use_case_result["messages"][-1].content
                    progress_log += f"### Use Case Output:\n{use_case_content}\n\n"
                    time.sleep(1)

                    # Step 3: Collect Resources
                    yield "Step 3: Collecting Resources..."
                    resource_messages = [HumanMessage(content=f"Use Case Input: {use_case_content}")]
                    resource_state = {"messages": resource_messages}
                    resource_result = resource_agent.graph.invoke(resource_state)
                    resource_content = resource_result["messages"][-1].content
                    progress_log += f"### Resource Output:\n{resource_content}\n\n"
                    file_path = save_resources_to_file(resource_content)
                    progress_log += f"**Resources saved at:** {file_path}\n\n"
                    time.sleep(1)

                    # Final Output
                    progress_log += "### Process Completed Successfully!"
                    yield progress_log
                except Exception as e:
                    progress_log += f"Error occurred: {e}"
                    yield progress_log

            # Connect buttons
            submit_button.click(gradio_interface_with_progress, inputs=[query], outputs=[output])

        # Launch Gradio UI
        demo.launch(server_name="0.0.0.0", server_port=7860)

    except CustomException as e:
        logger.error("Problem with frontend service")
        raise CustomException("Failed to start frontend", e)


if __name__ == "__main__":
    try:
        threading.Thread(target=run_backend).start()
        time.sleep(2)
        run_frontend()
    except CustomException as e:
        logger.exception(f"CustomException occurred: {str(e)}")
