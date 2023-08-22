#WRITTEN BY DX.RONI
#---------import---------#
#---------color---------#
bblack="\033[1;30m"       #Black
M="\033[1;31m"       #Red
H="\033[1;32m"       #Green
byellow="\033[1;33m"       #Yellow
bblue="\033[1;34m"       #Blue
P="\033[1;35m"       #Purple
C="\033[1;36m"       #Cyan
B="\033[1;37m"       #white
my_color = [
B,C,P,H]
warna = random.choice(my_color)
#---------logo---------#
logo=("""╔══════════════════════════════════╗
║\033[38;5;46m███╗░░██╗\33[38;5;196m██╗\033[34;1m██╗░░██╗\033[38;5;46m░█████╗\33[38;5;196m░███╗░░██╗
║\033[38;5;46m████╗░██║\33[38;5;196m██║\033[34;1m██║░░██║\033[38;5;46m██╔══██╗\033[38;5;46m████╗░██║
║\033[38;5;46m██╔██╗██║\33[38;5;196m██║\033[34;1m███████║\033[38;5;46m███████║\33[38;5;196m██╔██╗██║
║\033[38;5;46m██║╚████║\33[38;5;196m██║\033[34;1m██╔══██║\033[38;5;46m██╔══██║\033[38;5;46m██║╚████║
║\033[38;5;46m██║░╚███║\33[38;5;196m██║\033[34;1m██║░░██║\033[38;5;46m██║░░██║\33[38;5;196m██║░╚███║
║\033[38;5;46m╚═╝░░╚══╝\33[38;5;196m╚═╝\033[34;1m╚═╝░░╚═╝\033[38;5;46m╚═╝░░╚═╝\033[38;5;46m╚═╝░░╚══╝
║
╚═════════════════
{warna}-----------------------------------------{B}
Owner   :{C}  DX RONI  {B}
Guthub   :GX NIHAN 404
Facebook   :DX RONI CHOWDHURY
Tools   : RANDOM CLONING
{warna}-----------------------------------------{B}""")
#---------linex def---------#
 #  print(f'{warna}-------------------------{B}')
   #---------clear def---------#
   def clear():
	clr('clear')
	print(logo)
#---------main def---------#def DX_RONI():
	clear()
	print(f'{B} [{warna}01{B}] RANDOM CLONING')
	print(f'{B} [{warna}00{B}] EXIT TERMINAL')
	option=input(f' {B}[{warna}??{B}] CHOICE MENU >>')
	if option in ['01','1']:
		BD_CLONING()
	else:
		exit('thanks for video using dear :)')
#---------bd clone def---------#
def BD_CLONING():
	print ('NEXT PART ABD CLONING FUNCTION/DEF NIYA KAJ KORBO :)')
	exit()
#---------end---------#

DX_RONI()