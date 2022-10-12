import csv
import sys

#assuming file format : lastname,firstname,phonenumber,mail
with open( "assets/rakshins.csv", 'r' ) as source:
     reader = csv.reader(source)
     i = 0

     for row in reader:
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

      i += 1

      allvcf.close()
      print (str(i) + " vcf cards generated.")

def main(args):
     if len(args) != 2:
          print ( "Usage:")
          print ( args[0] + " filename")
          return

     convert(args[1])

if __name__ == '__main__':
    main(sys.argv)
