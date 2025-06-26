from typing import Annotated

from pydantic import BaseModel
from fastapi import Depends

from server.src.models import SubPlans
from server.src.config import settings


class PlanConfig(BaseModel):
    max_prompts: int
    max_versions: int


class SubscriptionManager:
    SUBSCRIPTION_PLANS: dict[SubPlans, PlanConfig] = {
        SubPlans.trial: PlanConfig(
            max_prompts=settings.sub.trial_max_prompts,
            max_versions=settings.sub.trial_versions_limit,
        ),
        SubPlans.basic: PlanConfig(
            max_prompts=settings.sub.basic_max_prompts,
            max_versions=settings.sub.basic_versions_limit,
        ),
        SubPlans.standard: PlanConfig(
            max_prompts=settings.sub.standard_max_prompts,
            max_versions=settings.sub.standard_versions_limit,
        ),
        SubPlans.premium: PlanConfig(
            max_prompts=settings.sub.premium_max_prompts,
            max_versions=settings.sub.premium_versions_limit,
        ),
    }
    async def get_plan_info(self, plan: SubPlans) -> PlanConfig:
        return self.SUBSCRIPTION_PLANS.get(plan)


async def get_sub_manager() -> SubscriptionManager:
    return SubscriptionManager()


sub_manager_depc = Annotated[SubscriptionManager, Depends(get_sub_manager)]