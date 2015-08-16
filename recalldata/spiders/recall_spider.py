__author__ = 'yandong'
import scrapy
import codecs
from recalldata.items import RecallDataItem

def findalldollarsigns(str):
    list=[]
    where=0
    while str.find('$',where) !=-1:
        where=str.find('$',where)
        if not str[where+1].isdigit():
         list.append(where)
        where=where+1
    counter=0
    newstr=str
    print list
    for x in list:
        newstr=newstr[:x-counter]+newstr[x+1-counter:]
        print newstr
        counter=counter+1
    return newstr
print findalldollarsigns('About $ty $50')

def unitConvert(str):
    if ('hundred') in str:
        return 100
    if ('thousand') in str:
        return 1000
    if ('million') in str:
        return 1000000
    if ('billion') in str:
        return 1000000000
    if ('trillion') in str:
        return 1000000000000
    else:
        return "FAIL"
def findnextdigit(str,index):
    for x in range (index,len(str)):
        if str[x].isdigit():
            return x
    return "None"
def findlastdigit(str,index):
    flippy = False
    firstdigit=findnextdigit(str,index)
    for x in range (firstdigit,len(str)):
        if not (str[x].isdigit() or str[x]=='.'):
            return x
    return "None"

def numberfinder(str,int):
    number=""

    if (str.find('hundred',int)>-1 or str.find('thousand',int)>-1 or str.find('million',int)>-1) and (str[findlastdigit(str,int)+1] == 'h' or str[findlastdigit(str,int)+1]=='t' or str[findlastdigit(str,int)+1] == 'm') :
        print "brug"
        for x in range (findnextdigit(str,int),len(str)):
            if (str[x].isdigit() or str[x]=='.'):
                number=number+str[x]
               # print 'ezt'
            elif str[x] == ' ' and x>0:
               # print "x"
               # print x
                firstspace = str.find(" ",x+1)
              #  print firstspace>0
               # print "firstspace^"
                firstperiod = str.find(".",x+1)
               # print firstperiod>0
              #  print "firstperiod^"

                if firstspace>0 and firstperiod<0 or firstspace<0 and firstperiod>0 :
                   # print "bop"
                    wordend = max(firstspace,firstperiod)
                else:
                    wordend=min(firstspace,firstperiod)
                if wordend == -1:
                    wordend = len(str)
                units=unitConvert(str[x+1:wordend])
                print str[x+1:wordend]
                print 'ezt1'
                if units == 'FAIL':
                    print 'ABORT MISSION UNITS NOT FOUND'
                whatigot = float(number)*float(units)
                #print wordend
                #print whatigot
                return [whatigot,wordend]
            elif str[x] == ',':
               # print ('this is a comma')
                continue
            else:
               # print 'ezt2'
                return "No Numbers"
    else:
        for x in range (findnextdigit(str,int),len(str)):
            if (str[x].isdigit()):
                print "a number"
                number=number+str[x]
            #elif (x>0 and str[x-1].isdigit() and str[x]==' ')
            elif str[x] == ',':
                #print ('this is a comma')
                continue


            elif str[x] == " ":
                #print "a space"
                continue
            elif number != "":
                #print "i got something"
                return [number,x]
        if number != "":
            return [number,x]
        else:
            return "none"







def getnumberofunits(str):
    if str.isdigit() and float(str)<10:
        return float(str)
    if str.find("worldwide") > -1:
        x = str.find("worldwide")
        while not str[x].isdigit():
            x=x-1
        while str[x].isdigit() or str[x]=='.':
            x=x-1
       # print str[x+1:]
        #print "austg"
        return numberfinder(str,x+1)[0]

    allprices=[]
    whereami = 0
    while findnextdigit(str,whereami) != "None" and numberfinder(str,whereami) != "No Numbers" and whereami != len(str)-1:
        print "entered while"
        info = numberfinder(str,whereami)
        print info
        allprices.append(float(info[0]))
        whereami=info[1]
        print "a new day"
    print allprices
    return sum(allprices)

def exists(list):
    if list:
        return list[0]
    else:
        return "NULL"

def getRetailPrice(str):
    actualstr=findalldollarsigns(str)
    print "checking "+actualstr
    if actualstr.find('$') == -1:
        return "NoRetailPriceFound"
    else:
        price1=""
        price2=""
        flipper = True
        for x in range (actualstr.find('$')+1,len(actualstr)):
            if actualstr[x].isdigit() and flipper:
                price1=price1+actualstr[x]
            elif actualstr[x].isdigit() and not flipper:
                price2=price2+actualstr[x]
            elif (actualstr[x] == ','):
                continue
            elif actualstr.find('$', x) == -1 and flipper:
                return '$'+price1
            elif not actualstr.find('$',x) == -1:
                print "o.o"
                flipper = False
                continue
            else:
                break
        if price1=='' and price2=='':
            return "NoRetailPriceFound"
        return '$'+price1+" to $"+price2

#print getRetailPrice(('buybuy Baby, ToysRUs BabiesRUs and independent specialty stores nationwide and online at Amazon.com from September 2014 through April 2015 for about $55.').encode('ascii','ignore'))
#print getnumberofunits('About 4.6 million units in the U.S. and 175,000 in Canada')
#numberfinder('blah blah 5,577,000 in the U.S. and 446,700 in Canada',0)


class RecallSpider(scrapy.Spider):
    name = "recalldata"
    allowed_domains = ["saferproducts.gov"]
    start_urls = ["http://www.saferproducts.gov/RestWebServices/Recall/?RecallDate=2014"]




    def parse(self,response):
        recallcount=0
        productcount = 0
        tempdict=dict()
        item = RecallDataItem()
        thisrecall=dict()
        for recall in response.xpath('Recall'):
            recallID=exists(recall.xpath('./RecallID/text()').extract())
            thisrecall.update({str(recallcount)+"RecallID":recallID})
            recallDate= exists(recall.xpath('./RecallDate/text()').extract())
            thisrecall.update({str(recallcount)+"Date":recallDate})


            thisrecall.update({str(recallcount)+'Description':exists(recall.xpath('./Description/text()').extract()).replace('\n',' ')})
            thisrecall.update({str(recallcount)+'Title' :exists(recall.xpath('./Title/text()').extract()).replace('\n',' ')})
            for product in recall.xpath('.//Products/Product'):
                productkey=str(recallcount) + "Product" + "%d" % (productcount)
                print productkey
               # print "what if jame lao were ezt"
               # print product
               # print product.xpath('.//Name/text()').extract()
                if product.xpath('.//Name/text()').extract():
                    thisrecall.update({productkey:str(product.xpath('.//Name/text()').extract()[0].encode('ascii', 'ignore')).replace('\n',' ')})
                else:
                    thisrecall.update({productkey:"NO NAME"})
                #print product.xpath('./NumberOfUnits/text()').extract()

                if not product.xpath('.//NumberOfUnits/text()').extract():
                    numberofunits=0
                else:
                    #print product.xpath('./NumberOfUnits/text()').extract()
                    if recallcount == 1186:
                        thisrecall.update({str(recallcount)+"UnitNumbers"+"%d" %(productcount):1000000})
                    else:
                        print "checking units of this sentence" + str(product.xpath('.//NumberOfUnits/text()').extract()[0].encode('ascii', 'ignore'))
                        numberofunits=getnumberofunits(str(product.xpath('.//NumberOfUnits/text()').extract()[0].encode('ascii', 'ignore')))
                        print str(product.xpath('.//NumberOfUnits/text()').extract()[0].encode('ascii', 'ignore'))
                numberkey=str(recallcount)+"UnitNumbers"+"%d" %(productcount)
                thisrecall.update({numberkey:numberofunits})
                #print "end product"
                productcount=productcount+1
            productcount = 0
            injurycount = 0
            for injury in recall.xpath('.//Injuries/Injury'):
                injurykey = str(recallcount)+"Injury"+"%d" %(injurycount)
                thisrecall.update({ injurykey :exists(injury.xpath('./Name/text()').extract()).replace('\n',' ')})
                injurycount=injurycount+1
            injurycount = 0
            manufacturercount = 0
            for manufacturer in recall.xpath('.//ManufacturerCountries/ManufacturerCountry'):
                manufacturerkey=str(recallcount)+"Country"+"%d" %(manufacturercount)
                thisrecall.update({  manufacturerkey :exists(manufacturer.xpath('./Country/text()').extract()).replace('\n',' ')})
                manufacturercount=manufacturercount+1
            manufacturercount = 0
            hazardcount = 0
            for hazard in recall.xpath('.//Hazards/Hazard'):
                hazardkey=str(recallcount)+"Hazard"+"%d" %(hazardcount)
                thisrecall.update({ hazardkey :exists(hazard.xpath('./Name/text()').extract()).replace('\n',' ')})
                hazardcount = hazardcount+1
            remedycount = 0
            for remedy in recall.xpath('.//Remedies/Remedy'):
                remedykey=str(recallcount)+"Remedy"+"%d" % (remedycount)
                thisrecall.update({ remedykey :exists(remedy.xpath('./Name/text()').extract()).replace('\n',' ')})
                remedycount = remedycount+1
            retailercount=0
            for retailer in recall.xpath('.//Retailers/Retailer'):
                print "ezt789"
                retailerkey=str(recallcount)+"Retailer"+"%d" % (retailercount)
                thisrecall.update({ retailerkey :exists(retailer.xpath('./Name/text()').extract()).replace('\n',' ')})
                retailerprice=str(recallcount)+"RetailerPrice"+"%d" % (retailercount)
                thisrecall.update({retailerprice:getRetailPrice(exists(retailer.xpath('./Name/text()').extract()).replace('\n',' '))})
                print "found "+ getRetailPrice(exists(retailer.xpath('./Name/text()').extract()).replace('\n',' '))
                retailercount = retailercount+1


            tempdict.update(thisrecall)

            #print "end for"
            recallcount=recallcount + 1
           # print recallcount
        item['recalldata2014']=tempdict
       # print item
        return item



















