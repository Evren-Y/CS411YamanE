from typing import Any, Optional

from wildlife_tracker.habitat_management.habitat import Habitat

class Migration:

    def __init__(self, 
                 migration_id: int, 
                 species: str, 
                 start_location: Habitat, 
                 destination: Habitat, 
                 start_date: str, 
                 current_date: str, 
                 current_location: str,
                 duration: Optional[int] = None,
                 status: str = "Scheduled") -> None:
        self.migration_id = migration_id
        self.species = species
        self.start_location = start_location
        self.destination = destination
        self.start_date = start_date
        self.current_date = current_date
        self.current_location = current_location
        self.duration = duration
        self.status = status
            
    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass

    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass