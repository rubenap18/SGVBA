from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

class MainView:
    def __init__(self):
        self.console = Console()

    def show_welcome_message(self):
        """Muestra un panel de bienvenida estilizado."""
        self.console.print(
            Panel(
                "[bold green]Bienvenido al Sistema Gestor de Ventas de Boletos de Autobús[/bold green]\n:bus: [cyan]Transportes Cuervo Negro[/cyan] :bus:",
                title="SGVBA",
                border_style="blue"
            )
        )

    def show_main_menu(self) -> str:
        """Muestra el menú principal y solicita una opción al usuario."""
        self.console.print("\n[bold]Menú Principal[/bold]")
        self.console.print("1. Portal de Clientes")
        self.console.print("2. Portal de Administración")
        self.console.print("3. Salir")
        
        choice = Prompt.ask("Selecciona una opción", choices=["1", "2", "3"], default="3")
        return choice

    def run(self):
        """Inicia el bucle principal de la aplicación de consola."""
        self.show_welcome_message()
        
        while True:
            choice = self.show_main_menu()
            
            if choice == '1':
                self.console.print("\n[bold yellow]Iniciando Portal de Clientes...[/bold yellow]")
                # Aquí se llamaría al controlador/vista de clientes
                # Por ahora, solo es un marcador de posición
                self.console.print("Funcionalidad de cliente aún no implementada.", style="italic red")
            
            elif choice == '2':
                self.console.print("\n[bold yellow]Iniciando Portal de Administración...[/bold yellow]")
                # Aquí se llamaría al controlador/vista de administración
                # Por ahora, solo es un marcador de posición
                self.console.print("Funcionalidad de administración aún no implementada.", style="italic red")

            elif choice == '3':
                break
        
        self.console.print("\nGracias por usar Transportes Cuervo Negro. ¡Hasta pronto!\n")
