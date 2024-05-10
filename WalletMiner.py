import string, random, colorama


from colorama import Fore, Back, Style


colorama.init()



text = " 0xlsie4d"


address=print('''
      ** **               **                               
     /**/**              /**      **   **  **   **  **   **
     /**/**        ******/**  ** //** **  //** **  //** ** 
     /**/**       **//// /** **   //***    //***    //***  
     /**/**      //***** /****     /**      /**      /**   
 **  /**/**       /////**/**/**    **       **       **    

//***** /******** ****** /**//**  **       **       **                  


 /////  //////// //////  //  //  //       //       //   
 \n\n\n''')
 

address=input("  WALLET : ")




while True:

    print((Fore.WHITE + " [+] ") + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(52)) + (Fore.RED + " - 0.0000 ETH"))
