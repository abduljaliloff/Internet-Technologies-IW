from django import forms
from .models import Player, Team

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['team', 'full_name', 'age', 'position', 'jersey_number', 'market_value', 'is_injured']
    
    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_injured':
                field.widget.attrs.update({'class': 'modern-input'})
        
        self.fields['team'].empty_label = "Select a Club" 
        self.fields['team'].queryset = Team.objects.all() 