import win32ui
dlg = win32ui.CreateFileDialog(1)
dlg.DoModal()

filepath = dlg.GetPath()
filename = dlg.GetPathName()
print(filepath)

