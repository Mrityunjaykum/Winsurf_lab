from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from graph_logic.state import ClaimState
from graph_logic.nodes import claim_validation_node, fraud_detection_node, recommendation_node
 
workflow = StateGraph(ClaimState)
 
workflow.add_node("validator", claim_validation_node)
workflow.add_node("fraud", fraud_detection_node)
workflow.add_node("recommendation", recommendation_node)
 
workflow.set_entry_point("validator")
workflow.add_edge("validator", "fraud")
workflow.add_edge("fraud", "recommendation")
 
def router(state: ClaimState):
    return "manual_review" if state["recommendation"] == "MANUAL_REVIEW" else END
 
workflow.add_conditional_edges("recommendation", router, {"manual_review": "manual_review", "end": END})
workflow.add_node("manual_review", lambda x: {"final_decision": "PENDING_HUMAN"})
 
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)