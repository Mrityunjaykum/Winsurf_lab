from graph_logic.state import ClaimState
 
def claim_validation_node(state: ClaimState):
    status = "PASS" if state["claim_amount"] > 0 else "FAIL"
    return {"validation_status": status, "audit_log": ["Validated fields."]}
 
def fraud_detection_node(state: ClaimState):
    score = 80.0 if state["claim_amount"] > 50000 else 20.0
    return {"fraud_score": score, "audit_log": ["Fraud check performed."]}
 
def recommendation_node(state: ClaimState):
    if state["fraud_score"] > 60:
        return {"recommendation": "MANUAL_REVIEW", "recommendation_reason": "High fraud risk"}
    return {"recommendation": "APPROVED", "recommendation_reason": "Low risk"}