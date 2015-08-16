# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class RecalldataPipeline(object):
    def process_item(self,item,spider):
        file=open("recalldata.txt",'w')
        recalldict=item['recalldata2014']
        print "ezt 69"
        #print recalldict
        counter=0
        while str(counter)+"RecallID" in recalldict:
            print "hello?"
            #print recalldict[str(counter)+"RecallDate"]
            file.write(str(recalldict[str(counter)+"RecallID"].encode("utf-8"))+"^"+str(recalldict[str(counter)+"Date"].encode("utf-8"))+"^"+str(recalldict[str(counter)+"Description"].encode("utf-8"))+"^"+str(recalldict[str(counter)+"Title"].encode("utf-8"))+"^")
            productcount=0
            while str(counter)+"Product"+str(productcount) in recalldict or str(counter)+"UnitNumbers"+str(productcount) in recalldict:
                #print 'ezt!'
                #print recalldict[str(counter)+"Product"+str(productcount)]
               # print recalldict[str(counter)+"UnitNumbers"+str(productcount)]

                if not (recalldict[str(counter)+"UnitNumbers"+str(productcount)]) and recalldict[str(counter)+"Product"+str(productcount)]:
                    file.write(str(recalldict[str(counter)+"Product"+str(productcount)].encode("utf-8"))+"^"+"None"+"^")
                elif not recalldict[str(counter)+"Product"+str(productcount)]  and recalldict[str(counter)+"UnitNumbers"+str(productcount)]:
                    file.write("No product name"+"^"+str(recalldict[str(counter)+"UnitNumbers"+str(productcount)].encode("utf-8"))+"^")
                elif recalldict[str(counter)+"UnitNumbers"+str(productcount)] and recalldict[str(counter)+"Product"+str(productcount)]:
                    print recalldict[str(counter)+"Product"+str(productcount)]
                    print recalldict[str(counter)+"UnitNumbers"+str(productcount)]
                    file.write(str(recalldict[str(counter)+"Product"+str(productcount)].encode("utf-8"))+"^"+str(recalldict[str(counter)+"UnitNumbers"+str(productcount)]).encode("utf-8")+"^")
                else:
                    file.write("No product name,"+"None")
                productcount=productcount+1
            versatilecount=0
            while str(counter)+"Injury"+str(versatilecount) in recalldict:
                file.write(str(recalldict[str(counter)+"Injury"+str(versatilecount)].encode("utf-8"))+"^")
                versatilecount=versatilecount+1
            versatilecount=0
            while str(counter)+"Country"+str(versatilecount) in recalldict:
                file.write(str(recalldict[str(counter)+"Country"+str(versatilecount)].encode("utf-8"))+"^")
                versatilecount=versatilecount+1
            versatilecount=0
            while str(counter)+"Hazard"+str(versatilecount) in recalldict:
                file.write(str(recalldict[str(counter)+"Hazard"+str(versatilecount)].encode("utf-8"))+"^")
                versatilecount=versatilecount+1
            versatilecount=0
            while str(counter)+"Remedy"+str(versatilecount) in recalldict:
                file.write(str(recalldict[str(counter)+"Remedy"+str(versatilecount)].encode("utf-8"))+"^")
                versatilecount=versatilecount+1
            versatilecount=0
            while str(counter)+"Retailer"+str(versatilecount) in recalldict:
                print "austin"
                file.write(str(recalldict[str(counter)+"Retailer"+str(versatilecount)].encode("utf-8"))+"^")
                versatilecount=versatilecount+1
            versatilecount=0
            while str(counter)+"RetailerPrice"+str(versatilecount) in recalldict:
                print "austin1"
                file.write(str(recalldict[str(counter)+"RetailerPrice"+str(versatilecount)].encode("utf-8"))+"^")
                versatilecount=versatilecount+1
            file.write("\n")
            counter=counter+1
        return recalldict

