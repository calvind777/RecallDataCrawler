__author__ = 'yandong'
class recallDataPipeline(object):


    def process_item(self,item,spider):
        file=open("recalldata",'w')
        recalldict=item['recalldata2014']
        counter=0
        while str(counter)+"RecallID" in recalldict:
            file.write(recalldict[str(counter)+"RecallID"].encode('ascii', 'ignore')+","+recalldict[str(counter)+"Date"].encode('ascii', 'ignore')+","+recalldict[str(counter)+"Description"].encode('ascii', 'ignore')+","+recalldict[str(counter)+"Title"].encode('ascii', 'ignore')+",")
            productcount=0
            while str(counter)+"Product"+productcount in recalldict:
                file.write(recalldict[str(counter)+"Product"+productcount].encode('ascii', 'ignore')+","+recalldict[str(counter)+"UnitNumbers"+productcount].encode('ascii', 'ignore')+",")
                productcount=productcount+1
            versatilecount=0
            while str(counter)+"Injury"+versatilecount in recalldict:
                file.write(recalldict[str(counter)+"Injury"+versatilecount].encode('ascii', 'ignore')+",")
                versatilecount=versatilecount+1
            versatilecount=0
            while str(counter)+"Country"+versatilecount in recalldict:
                file.write(recalldict[str(counter)+"Country"+versatilecount].encode('ascii', 'ignore')+",")
                versatilecount=versatilecount+1
            versatilecount=0
            while str(counter)+"Hazard"+versatilecount in recalldict:
                file.write(recalldict[str(counter)+"Hazard"+versatilecount].encode('ascii', 'ignore')+",")
                versatilecount=versatilecount+1
            versatilecount=0
            while str(counter)+"Remedy"+versatilecount in recalldict:
                file.write(recalldict[str(counter)+"Remedy"+versatilecount].encode('ascii', 'ignore')+",")
                versatilecount=versatilecount+1
            versatilecount=0
            file.write("\n")
            counter=counter+1
        return recalldict
