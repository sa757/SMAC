from .q_learner import QLearner
from .coma_learner import COMALearner
from .qtran_learner import QLearner as QTranLearner
from .LIIR_Learner import LIIRLearner
from .latent_q_learner import LatentQLearner

REGISTRY = {}

REGISTRY["q_learner"] = QLearner
REGISTRY["coma_learner"] = COMALearner
REGISTRY["qtran_learner"] = QTranLearner
REGISTRY["liir_learner"] = LIIRLearner
REGISTRY['latent_q_learner'] =LatentQLearner