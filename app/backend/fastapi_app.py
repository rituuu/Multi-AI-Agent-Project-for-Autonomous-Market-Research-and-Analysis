from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from typing import Optional
from Multi_Agents.MultiAgents import multi_agent_workflow

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(
    title="Multi-Agent Market Research API",
    description="FastAPI endpoint for running the multi-agent workflow defined in agents.py",
    version="1.0.0"
)

# Define request model
class QueryRequest(BaseModel):
    query: str

# Define response model (optional for clarity)
class QueryResponse(BaseModel):
    status: str
    query: str
    research_output: str
    use_cases_output: str
    resources_output: str
    saved_file: Optional[str] = None


@app.post("/generate_insights", response_model=QueryResponse)
async def generate_insights(request: QueryRequest):
    """
    Run the full multi-agent market research pipeline.
    Uses existing multi_agent_workflow() from agents.py
    """
    try:
        logger.info(f"Received request for query: {request.query}")
        
        # Unpack the tuple returned by multi_agent_workflow
        research_output, use_cases_output, resources_output, saved_file = multi_agent_workflow(request.query)

        return QueryResponse(
            status="success",
            query=request.query,
            research_output=research_output,
            use_cases_output=use_cases_output,
            resources_output=resources_output,
            saved_file=saved_file
        )
    except Exception as e:
        logger.error(f"Error occurred while processing query: {e}")
        raise HTTPException(status_code=500, detail=str(e))
