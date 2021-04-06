from django import template
register = template.Library()

@register.filter(name='only_username')
def only_username(email):
   # print(type(email))
   return email.__str__().split('@')[0]

@register.filter(name='preference_empty')
def preference_empty(preference):
   result = None
   print(preference)
   # if len(preference_list) == 0:
   #    result = True
   # else:
   #    result = False
   return "test"

@register.filter(name='is_empty')
def is_empty(any_list):
   empty = False
   if len(any_list) < 1:
      empty = True
   return empty
