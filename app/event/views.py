from django.shortcuts import render
from .models import Event

# Create your views here.

def create_event(request):
    # Create  event
    event = Event.objects.create(
        content={"key": "value"},
    )
    # Update event
    event.content = {"key": "new_value"}

    # Save event
    event.save()

    # Render index.html
    return render(request, "event/index.html")