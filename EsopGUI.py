#!/usr/bin/env python
# -*- coding: CP1252 -*-
#
# generated by wxGlade 0.6.8 (standalone edition) on Wed Feb 05 21:56:15 2014
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class ESOP(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ESOP.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.label_1 = wx.StaticText(self, wx.ID_ANY, _("This is a test question for the program to use to fill up space"))
        self.radio_btn_3 = wx.RadioButton(self, wx.ID_ANY, _("1"))
        self.radio_btn_4 = wx.RadioButton(self, wx.ID_ANY, _("2"))
        self.radio_btn_5 = wx.RadioButton(self, wx.ID_ANY, _("3"))
        self.radio_btn_6 = wx.RadioButton(self, wx.ID_ANY, _("4"))
        self.radio_btn_7 = wx.RadioButton(self, wx.ID_ANY, _("5"))
        self.radio_btn_8 = wx.RadioButton(self, wx.ID_ANY, _("YES"), style=wx.RB_GROUP)
        self.radio_btn_9 = wx.RadioButton(self, wx.ID_ANY, _("NO"))
        self.button_1 = wx.Button(self, wx.ID_ANY, _("\nNext\n"))
        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ESOP.__set_properties
        self.SetTitle(_("esop1"))
        self.SetSize((627, 250))
        self.SetBackgroundColour(wx.Colour(25, 255, 5))
        self.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.label_1.SetMinSize((611, 75))
        self.label_1.SetBackgroundColour(wx.Colour(175, 255, 216))
        self.radio_btn_3.SetMinSize((75, 26))
        self.radio_btn_3.Hide()
        self.radio_btn_4.SetMinSize((75, 26))
        self.radio_btn_5.SetMinSize((75, 26))
        self.radio_btn_6.SetMinSize((75, 26))
        self.radio_btn_7.SetMinSize((75, 26))
        self.radio_btn_8.Hide()
        self.radio_btn_9.Hide()
        self.button_1.SetMinSize((75, 50))
        self.button_1.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ESOP.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.label_1, 8, wx.ALL, 0)
        sizer_2.Add(self.radio_btn_3, 0, wx.EXPAND, 0)
        sizer_2.Add(self.radio_btn_4, 0, wx.EXPAND, 0)
        sizer_2.Add(self.radio_btn_5, 0, wx.EXPAND, 0)
        sizer_2.Add(self.radio_btn_6, 0, wx.EXPAND, 0)
        sizer_2.Add(self.radio_btn_7, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_1.Add(sizer_2, 3, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_3.Add(self.radio_btn_8, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_3.Add(self.radio_btn_9, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_1.Add(sizer_3, 1, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_1.Add(self.button_1, 0, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 11)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class ESOP
class Esop(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        esopFrame = ESOP(None, wx.ID_ANY, "")
        self.SetTopWindow(esopFrame)
        esopFrame.Show()
        return 1

# end of class Esop

if __name__ == "__main__":
    gettext.install("esop") # replace with the appropriate catalog name

    esop = Esop(0)
    esop.MainLoop()