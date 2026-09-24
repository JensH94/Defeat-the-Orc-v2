from print_style import slow_print


def show_status(entity_group, title, show_resource=True):
    slow_print(f"-- {title} --")
    for entity in entity_group:
        slow_print(f"Name:{entity.name}|HP:{entity.current_health}/{entity.base_health}")
        if show_resource:
            slow_print(f"|Resource:{entity.current_resource}/{entity.max_resource}/{entity.resource_type.capitalize()}")
        for effect in entity.entity_effects:
            slow_print(f"{effect.name}|{effect.effects_duration}")