from django.core.management.base import BaseCommand
from datetime import datetime

from seed.load_vehicle_data import load_vehicle_data
from seed.load_maintenance_data import load_maintenance_data
from seed.load_services_data import load_services_data
from seed.load_service_appointment_data import load_service_appoinment_data
from seed.load_appointment_data import load_appointment_data
from seed.load_detail_data import load_detail_data


class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')

        # Load data from file
        from business_intelligence.models import Vehicle
        if not Vehicle.objects.exists():
            vehicle_data = load_vehicle_data()

            # Crea y guarda los objetos Vehicle
            for data in vehicle_data:
                Vehicle.objects.create(
                    brand=data['brand'],
                    model=data['model'],
                    year=data['year'],
                    vin=data['vin'],
                    licensePlate=data['licensePlate']
                )
                # Opcional: Puedes imprimir los vehículos creados
                # self.stdout.write(self.style.SUCCESS(f'Created Vehicle: {vehicle}'))
            
            self.stdout.write(self.style.SUCCESS('Vehiculos seeded exitosamente!'))

         # Load services data from file
        from business_intelligence.models.models import Servicio
        if not Servicio.objects.exists():
            service_data = load_services_data()

            # Create and save Maintenance objects
            for data in service_data:
                Servicio.objects.create(
                    id=data['id'],
                    name=data['name'],
                    description=data['description']
                )

            self.stdout.write(self.style.SUCCESS('Servicios seeded exitosamente!'))

         # Load services data from file
        from business_intelligence.models.models import Cita
        if not Cita.objects.exists():
            appointment_data = load_appointment_data()

            # Create and save Maintenance objects
            for data in appointment_data:
                try:
                    vehicle = Vehicle.objects.get(vin=data['vin'])
                    
                    Cita.objects.create(
                        id=data['id'],
                        scheduleDate=data['scheduleDate'],
                        status=data['status'],
                        vehicle=vehicle
                    )
                except Vehicle.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Error: Vehicle with VIN {data["vin"]} does not exist.'))

            self.stdout.write(self.style.SUCCESS('Citas seeded exitosamente!'))


        # Load maintenance data from file
        from business_intelligence.models import Mantenimiento
        if not Mantenimiento.objects.exists():
            maintenance_data = load_maintenance_data()
            for data in maintenance_data:
                try:
                    vehicle = Vehicle.objects.get(vin=data['vin'])

                    # Convertir la fecha al formato YYYY-MM-DD
                    date_str = data['date']
                    date = datetime.strptime(date_str, "%Y/%m/%d").strftime("%Y-%m-%d")

                    appointment = Cita.objects.get(id=data['id_appointment'])

                    Mantenimiento.objects.create(
                        vehicle=vehicle,
                        appointment=appointment,
                        date=date,
                        status=data['status']
                    )
                except Vehicle.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Error: Vehicle with VIN {data["vin"]} does not exist.'))

            self.stdout.write(self.style.SUCCESS('Mantenimiento seeded exitosamente!'))

        # Load services data from file
        from business_intelligence.models.models import ServicioCita
        if not ServicioCita.objects.exists():
            service_appointment_data = load_service_appoinment_data()

            # Create and save Maintenance objects
            for data in service_appointment_data:
                try:
                    appointment = Cita.objects.get(id=data['id_appointment'])
                    service = Servicio.objects.get(id=data['id_service'])
                    ServicioCita.objects.create(
                        appointment=appointment,
                        service=service
                    )
                except (Cita.DoesNotExist, Servicio.DoesNotExist) as e:
                    self.stdout.write(self.style.ERROR(f'Error: {e}'))

            self.stdout.write(self.style.SUCCESS('Servicios de Citas seeded exitosamente!'))

        from business_intelligence.models import Detail
        if not Detail.objects.exists():
            detail_data = load_detail_data()

            # Create and save Maintenance objects
            for data in detail_data:
                try:
                    maintenance = Mantenimiento.objects.get(id=data['mantenimiento_id'])
                    Detail.objects.create(
                        maintenance=maintenance,
                        id=data['id'],
                        description=data['description'],
                        cost=data['cost']
                    )
                except Vehicle.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Error: Mantenimiento with id {data["mantenimiento_id"]} does not exist.'))

            self.stdout.write(self.style.SUCCESS('Detalles seeded exitosamente!'))
        
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
