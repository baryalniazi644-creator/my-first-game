import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.utils import get_color_from_hex

class AdvancedClickerGame(App):
    def build(self):
        self.score = 0
        self.time_left = 15  
        
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.time_label = Label(
            text=f"⏳ Time: {self.time_left}s", 
            font_size=32,
            bold=True,
            color=get_color_from_hex('#E74C3C')
        )
        
        self.score_label = Label(
            text="🏆 Score: 0", 
            font_size=36,
            bold=True,
            color=get_color_from_hex('#F1C40F')
        )
        
        self.btn = Button(
            text="🎯 TAP ME FAST!", 
            font_size=40,
            bold=True,
            background_normal='',
            background_color=get_color_from_hex('#3498DB')
        )
        self.btn.bind(on_press=self.add_score)
        
        self.layout.add_widget(self.time_label)
        self.layout.add_widget(self.score_label)
        self.layout.add_widget(self.btn)
        
        self.timer_event = Clock.schedule_interval(self.update_time, 1)
        
        return self.layout

    def add_score(self, instance):
        if self.time_left > 0:
            self.score += 1
            self.score_label.text = f"🏆 Score: {self.score}"
            random_colors = ['#2ECC71', '#9B59B6', '#E67E22', '#1ABC9C', '#E74C3C']
            instance.background_color = get_color_from_hex(random.choice(random_colors))

    def update_time(self, dt):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.text = f"⏳ Time: {self.time_left}s"
        else:
            Clock.unschedule(self.timer_event)
            self.time_label.text = "⏰ TIME'S UP!"
            self.btn.disabled = True
            self.btn.text = "GAME OVER"
            self.btn.background_color = get_color_from_hex('#95A5A6')
            
            self.restart_btn = Button(
                text="🔄 Play Again", 
                font_size=30,
                bold=True,
                background_normal='',
                background_color=get_color_from_hex('#2ECC71'),
                size_hint_y=0.3
            )
            self.restart_btn.bind(on_press=self.reset_game)
            self.layout.add_widget(self.restart_btn)

    def reset_game(self, instance):
        self.score = 0
        self.time_left = 15
        self.score_label.text = "🏆 Score: 0"
        self.time_label.text = f"⏳ Time: {self.time_left}s"
        self.btn.disabled = False
        self.btn.text = "🎯 TAP ME FAST!"
        self.btn.background_color = get_color_from_hex('#3498DB')
        self.layout.remove_widget(self.restart_btn)
        self.timer_event = Clock.schedule_interval(self.update_time, 1)

if __name__ == "__main__":
    AdvancedClickerGame().run()
