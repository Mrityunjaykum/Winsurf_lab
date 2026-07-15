from typing import TypedDict, List, Optional
 
class ClaimState(TypedDict):
    claim_id: str
    customer_name: str
    policy_number: str
    claim_amount: float
    validation_status: Optional[str]
    fraud_score: Optional[float]
    risk_level: Optional[str]
    recommendation: Optional[str]
    recommendation_reason: Optional[str]
    final_decision: Optional[str]
    audit_log: List[str]