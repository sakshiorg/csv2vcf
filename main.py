import csv
import sys



while True:
     print("Would you like to:\n1. Generate Vcards\n2. End Program")
     main_opt = int(input("Your Choice: "))

     if main_opt == 1:
         #assuming file format : lastname,firstname,phonenumber,mail
         with open( "assets/rakshins.csv", 'r' ) as source:

                reader = csv.reader( source )
            

                i = 0
                print("Do you want to write:\n 1. An individual Vcard \n 2. All Vcards in the file  ")
                type = int(input("Your choice:"))

                if type==1:
                    for row in reader:
                        #write in individual vcf
                        vcf = open(row[1] + ' ' + row[0] + ".vcf", 'w')
                        vcf.write( 'BEGIN:VCARD' + "\n")
                        vcf.write( 'VERSION:2.1' + "\n")
                        vcf.write( 'N:' + row[0] + ';' + row[1] + "\n")
                        vcf.write( 'FN:' + row[1] + ' ' + row[0] + "\n")
                        vcf.write( 'ORG:' + 'ATI' + "\n")
                        vcf.write( 'TEL;CELL:' + row[2] + "\n")
                        vcf.write( 'EMAIL:' + row[3] + "\n")
                        vcf.write( 'END:VCARD' + "\n")
                        vcf.write( "\n")
                        vcf.close()
                
                

            

                if type==2:

                    for row in reader:
                    #write in the "ALL.vcf" file.
                        allvcf = open('ALL.vcf', 'w')
                        allvcf.write( 'BEGIN:VCARD' + "\n")
                        allvcf.write( 'VERSION:2.1' + "\n")
                        allvcf.write( 'N:' + row[0] + ';' + row[1] + "\n")
                        allvcf.write( 'FN:' + "Bootcamp " + row[1] + ' ' + row[0] + "\n")
                        allvcf.write( 'ORG:' + 'Bootcamp' + "\n")
                        allvcf.write( 'TEL;CELL:' + row[2] + "\n")
                        allvcf.write( 'EMAIL:' + row[3] + "\n")
                        allvcf.write( 'END:VCARD' + "\n")
                        allvcf.write( "\n")

                

                i += 1

                allvcf.close()
                print (str(i) + " vcf cards generated.")


     if main_opt == 2: 
         print('Okay, see you soon!')
         break          

def main(args):
    if len(args) != 2:
        print ( "Usage:")
        print ( args[0] + " filename")
        return

    convert(args[1])

if __name__ == '__main__':
    main(sys.argv)