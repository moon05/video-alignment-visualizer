import wx
import linereader
import videofeature

PATH = "./config.txt"

class MyFrame(wx.Frame):
  def __init__(self, parent, id, title):
    wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, (750, 600))
    self.videoFileList = []
    self.videoPathList = []
    self.protocolNames = []
    self.protocolPaths = []
    self.alignPaths = []
    self.Number = 0
    
    self.videoFileList, self.videoPathList, self.protocolNames, self.protocolPaths, self.alignPaths  = linereader.configReader(PATH)
    
    panel = wx.Panel(self, -1)
    HBOX = wx.BoxSizer(wx.HORIZONTAL)
    VBOXLeft  = wx.BoxSizer(wx.VERTICAL)
    VBOXRight = wx.BoxSizer(wx.VERTICAL)
    
    ######## stuff for VBOXLeft ########
    self.fileNameVBOX = wx.ListBox(panel, 20, wx.DefaultPosition, (250, 300), self.videoFileList)
    self.protocolTextCtrl = wx.TextCtrl(panel, -1, '', size = (200 , 30))
    
    VBOXLeft.Add(self.fileNameVBOX, 0, wx.TOP | wx.CENTER, 100)
    VBOXLeft.Add(self.protocolTextCtrl, 1, wx.ALIGN_CENTER | wx.TOP, 50)
    self.fileNameVBOX.Bind(wx.EVT_LISTBOX, self.OnSelect_forProt, id=20)
    ######### stuff for VBOXRight #######
    self.subList = wx.ListCtrl(panel, 26, wx.DefaultPosition, (330, 350), style = wx.LC_REPORT | wx.BORDER_SUNKEN)
    self.subList.InsertColumn(0, "Protocol Sentences", width = 300)
    VBOXRight.Add(self.subList, 0, wx.TOP, 100)
    self.subList.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnSelect_forSubtitle, id=26)
    
    HBOX.Add(VBOXLeft, 1, wx.ALIGN_LEFT)
    HBOX.Add(VBOXRight, 1, wx.ALIGN_RIGHT)
    panel.SetSizer(HBOX)
  
  
  def DeleteItemsFromSubtitleListCtrl(self):
    """For emptying the ListCtrl Box each time a different file is selected"""
    
    current_items_count = self.subList.GetItemCount() - 1
    while ((current_items_count) >= 0) :
      self.subList.DeleteItem(current_items_count)
      current_items_count-=1


  def OnSelect_forProt(self, event):
    """Load the protocol sentences for the selected video."""

    index = event.GetSelection()
    self.Number = index
    self.protocolTextCtrl.SetValue(self.protocolNames[index])
    tempList = linereader.subReader(self.protocolPaths[index])
    reversedList = tempList[::-1]
    self.DeleteItemsFromSubtitleListCtrl()
    #self.subList.DeleteColumn(0)
    for i in range(len(reversedList)):
      self.subList.InsertStringItem(0, reversedList[i])
  
  
  def OnSelect_forSubtitle(self, event):
    """For playing the frames for the sentence user selects"""

    LineNumber = event.m_itemIndex
    print "This is the line you have selected: %d" %LineNumber
    print "This is your file selection: %s" % self.Number
    print "This is the name of the File: %s" % self.videoFileList[self.Number]
    videoPath = self.videoPathList[self.Number]
    protocolLines = linereader.subReader(self.protocolPaths[self.Number])
    sentenceIndexList, startTimingList, endTimingList = linereader.timingReader(self.alignPaths[self.Number])
    start_time = -1
    end_time = -1
    for i in range(len(sentenceIndexList)):
      print sentenceIndexList[i], LineNumber, start_time
      if sentenceIndexList[i] == LineNumber:
        if start_time == -1:
          start_time = startTimingList[i]
        end_time = endTimingList[i]
    print start_time, end_time
    Feature = videofeature.PlayVideo(videoPath, start_time, end_time)


class MyApp(wx.App):
  def OnInit(self):
    frame = MyFrame(None, -1, 'VISUALIZER.py')
    frame.Centre()
    frame.Show(True)
    return True


app = MyApp(0)
app.MainLoop()