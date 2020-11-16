from django import template
from sale_clothes.models import AdditionalData

register = template.Library()

@register.simple_tag
def get_additional_data(element_id, user_site):
	additional_data = AdditionalData.objects.filter(
		element_id=element_id, user_site__url_address=user_site).last()
	if additional_data:
		return additional_data
	else:
		return None


@register.simple_tag
def get_good_limit(list_goods, limit):
	return list_goods[:limit]