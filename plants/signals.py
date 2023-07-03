from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import PlantRecord, PlantState
from checkout.models import OrderLineItem
from .workflow_automation import planted_actions


@receiver(post_save, sender=OrderLineItem)
def create_plant_record_on_line_item_save(sender, instance, created, **kwargs):
    """
    Create plant record on order line item create
    """
    if created:
        for i in range(instance.quantity):
            PlantRecord.objects.create(plant=instance.plant,
                                       order=instance.order,
                                       location=instance.location)


@receiver(post_save, sender=PlantRecord)
def update_plant_record_on_create(sender, instance, created, **kwargs):
    """
    Populate plant_number from primary key on creation
    and take action based on workflow state changes
    """

    if created:
        plant_state = PlantState.objects.get(plant_state_name='pending')
        instance.plant_number = instance.id
        instance.plant_state = plant_state
        instance.save()

    if instance.plant_state.plant_state_name == 'planted':
        planted_actions(instance)
