"""Owner-adopted D1-D3 corrected diagnostic contracts.

This namespace is intentionally separate from every source-faithful and
production household/KFE path.
"""

from .boundary import (
    BoundaryViolation,
    ClosedFaceOutwardDriftError,
    FaceSummary,
    StateConstraintAssessment,
    assess_state_constraints,
    require_state_constraints,
)
from .contracts import AUTHORITY_ID, FLATTEN_ORDER, STATE_ORDER, CorrectedDiagnosticGrid
from .cost import (
    CostSubgradient,
    TransferKKTCheck,
    check_transfer_kkt,
    regularized_adjustment_cost,
    regularized_adjustment_cost_subgradient,
    regularized_scale,
)
from .generator import CorrectedGenerator, assemble_consumed_drift_generator
from .saved_controls import (
    SavedControlProvenance,
    SavedControlSnapshot,
    load_saved_control_set,
)

__all__ = [
    "AUTHORITY_ID",
    "FLATTEN_ORDER",
    "STATE_ORDER",
    "BoundaryViolation",
    "ClosedFaceOutwardDriftError",
    "CorrectedDiagnosticGrid",
    "CorrectedGenerator",
    "CostSubgradient",
    "FaceSummary",
    "SavedControlProvenance",
    "SavedControlSnapshot",
    "StateConstraintAssessment",
    "TransferKKTCheck",
    "assess_state_constraints",
    "assemble_consumed_drift_generator",
    "check_transfer_kkt",
    "load_saved_control_set",
    "regularized_adjustment_cost",
    "regularized_adjustment_cost_subgradient",
    "regularized_scale",
    "require_state_constraints",
]
