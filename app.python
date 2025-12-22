from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class PresupuestoApp(App):
    def build(self):
        self.title = "Gestor de Presupuesto"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # --- ENTRADAS DE DATOS ---
        layout.add_widget(Label(text="Ganancia mensual ($):", color=(1, 1, 1, 1)))
        self.ingreso = TextInput(text="8000", multiline=False, input_filter='float')
        layout.add_widget(self.ingreso)

        layout.add_widget(Label(text="Gastos fijos ($):"))
        self.gastos = TextInput(text="5500", multiline=False, input_filter='float')
        layout.add_widget(self.gastos)

        layout.add_widget(Label(text="Gasto extra ($):"))
        self.extra = TextInput(text="700", multiline=False, input_filter='float')
        layout.add_widget(self.extra)

        layout.add_widget(Label(text="Impuesto (%):"))
        self.impuesto_pct = TextInput(text="0", multiline=False, input_filter='float')
        layout.add_widget(self.impuesto_pct)

        layout.add_widget(Label(text="Ahorro ($):"))
        self.ahorro = TextInput(text="0", multiline=False, input_filter='float')
        layout.add_widget(self.ahorro)

        # --- BOTÓN CALCULAR ---
        btn_calc = Button(text="CALCULAR TOTAL", background_color=(0, 0.7, 0, 1), size_hint_y=None, height=100)
        btn_calc.bind(on_press=self.calcular)
        layout.add_widget(btn_calc)

        # --- RESULTADO ---
        self.resultado_label = Label(text="Toca el botón para calcular", bold=True, font_size='18sp')
        layout.add_widget(self.resultado_label)

        return layout

    def calcular(self, instance):
        try:
            ing = float(self.ingreso.text)
            gas = float(self.gastos.text)
            ext = float(self.extra.text)
            imp_p = float(self.impuesto_pct.text)
            aho = float(self.ahorro.text)

            ganancia_mensual = ing - gas
            
            if ganancia_mensual < ext:
                permitible = "Gasto extra: NO AUTORIZADO"
            else:
                permitible = "Gasto extra: AUTORIZADO"

            # Lógica de impuestos y ahorros
            subtotal = ganancia_mensual - ext
            valor_impuesto = (ganancia_mensual * (imp_p / 100))
            total_final = subtotal - valor_impuesto - aho

            res_text = (
                f"Estado: {'Ganancia' if total_final > 0 else 'Perdida'}\n"
                f"{permitible}\n"
                f"Total Final: ${total_final:.2f}"
            )
            self.resultado_label.text = res_text
        except ValueError:
            self.resultado_label.text = "Error: Ingresa solo números"

if __name__ == "__main__":
    PresupuestoApp().run()

