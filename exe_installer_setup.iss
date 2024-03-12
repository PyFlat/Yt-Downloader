; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "PyFlat Youtube Downloader"
#define MyAppVersion "1.3.1"
#define MyAppPublisher "PyFlat Studios"
#define MyAppExeName "main.exe"
#define MyAppIconFile "appdata/images/app-icon.ico"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
SignTool=signtool
AppId={{C07689AF-CD91-4D65-BF7E-33F6F1D6F556}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
LicenseFile=C:\Users\Johannes\Documents\GitHub\YT-Downloader\LICENSE
AllowNoIcons=yes
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
OutputDir=C:\Users\Johannes\Documents\GitHub\YT-Downloader\build
OutputBaseFilename=win_installer_v{#MyAppVersion}
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "german"; MessagesFile: "compiler:Languages\German.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Johannes\Documents\GitHub\YT-Downloader\build\exe.win-amd64-3.11\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Johannes\Documents\GitHub\YT-Downloader\build\exe.win-amd64-3.11\api-ms-win-core-console-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Johannes\Documents\GitHub\YT-Downloader\build\exe.win-amd64-3.11\api-ms-win-core-fibers-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Johannes\Documents\GitHub\YT-Downloader\build\exe.win-amd64-3.11\api-ms-win-eventing-provider-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Johannes\Documents\GitHub\YT-Downloader\build\exe.win-amd64-3.11\frozen_application_license.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Johannes\Documents\GitHub\YT-Downloader\build\exe.win-amd64-3.11\python3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Johannes\Documents\GitHub\YT-Downloader\build\exe.win-amd64-3.11\python311.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Johannes\Documents\GitHub\YT-Downloader\build\exe.win-amd64-3.11\appdata\*"; DestDir: "{app}\appdata"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\Johannes\Documents\GitHub\YT-Downloader\build\exe.win-amd64-3.11\lib\*"; DestDir: "{app}\lib"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\{#MyAppIconFile}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"; IconFilename: "{app}\{#MyAppIconFile}"
;Name: "{commonprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\{#MyAppIconFile}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon; IconFilename: "{app}\{#MyAppIconFile}"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[Code]
procedure EditIniFileIfNeeded;
var
  IniFilePath: string;
begin
  IniFilePath := ExpandConstant('{app}\appdata\config.ini');
  if FileExists(IniFilePath) then
  begin
    SetIniString('DEFAULT', 'first-use-since-update', 'True', IniFilePath);
  end;
end;
procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
    EditIniFileIfNeeded;
end;
