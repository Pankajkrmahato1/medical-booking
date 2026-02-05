from app.services.catalog_service import CatalogService
from app.services.pricing_service import PricingService
from app.services.discount_service import DiscountService
from app.services.discount_quota_service import DiscountQuotaService
from app.services.compensation_service import CompensationService
from app.services.final_outcome_service import FinalOutcomeService




catalog_service = CatalogService()
pricing_service = PricingService()
discount_service = DiscountService()
discount_quota_service = DiscountQuotaService()
compensation_service = CompensationService()
final_outcome_service = FinalOutcomeService()