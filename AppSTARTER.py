
import os
if os.path.isdir('databases') is False:
    os.mkdir('databases')
else:
    pass

   
from banking_menu import menu

    
test = menu()
test.mainloop()

        


