from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User
from django.db import connection
import os


class Command(BaseCommand):
    help = 'Inicializa o banco de dados com migrations e dados do backup'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Força a reinicialização mesmo se o banco já existir',
        )
        parser.add_argument(
            '--skip-data',
            action='store_true',
            help='Pula o carregamento dos dados do backup',
        )

    def handle(self, *args, **options):
        force = options['force']
        skip_data = options['skip_data']
        
        self.stdout.write(self.style.NOTICE('=== Conecta ZL - Bootstrap ==='))
        
        db_exists = self._check_database_exists()
        
        if db_exists and not force:
            self.stdout.write(self.style.SUCCESS(
                'Banco de dados já existe. Use --force para reinicializar.'
            ))
            return
        
        self.stdout.write(self.style.NOTICE('Executando migrations...'))
        call_command('migrate', verbosity=1)
        self.stdout.write(self.style.SUCCESS('Migrations aplicadas com sucesso!'))
        
        if not skip_data:
            backup_file = 'data_backup.json'
            if os.path.exists(backup_file):
                self.stdout.write(self.style.NOTICE(f'Carregando dados de {backup_file}...'))
                try:
                    call_command('loaddata', backup_file, verbosity=1)
                    self.stdout.write(self.style.SUCCESS('Dados carregados com sucesso!'))
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f'Aviso ao carregar dados: {e}'))
            else:
                self.stdout.write(self.style.WARNING(
                    f'Arquivo {backup_file} não encontrado. Pulando carregamento de dados.'
                ))
        
        self.stdout.write(self.style.NOTICE('Coletando arquivos estáticos...'))
        call_command('collectstatic', '--noinput', verbosity=0)
        self.stdout.write(self.style.SUCCESS('Arquivos estáticos coletados!'))
        
        self._show_summary()
    
    def _check_database_exists(self):
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM auth_user")
                return True
        except Exception:
            return False
    
    def _show_summary(self):
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('=== Bootstrap concluído! ==='))
        self.stdout.write('')
        
        try:
            user_count = User.objects.count()
            self.stdout.write(f'  Usuários: {user_count}')
        except Exception:
            pass
        
        self.stdout.write('')
        self.stdout.write('Próximos passos:')
        self.stdout.write('  1. Execute: python manage.py runserver 0.0.0.0:5000')
        self.stdout.write('  2. Acesse: http://localhost:5000')
        self.stdout.write('  3. Login admin: admin / (senha do backup)')
        self.stdout.write('')
