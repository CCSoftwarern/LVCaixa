unit Unit2;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, JvComponentBase,
  JvCreateProcess;

type
  TForm2 = class(TForm)
    Button1: TButton;
    JvCreateProcess1: TJvCreateProcess;
    Button2: TButton;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form2: TForm2;

implementation

{$R *.dfm}

procedure TForm2.Button1Click(Sender: TObject);
begin
//WinExec('cmd.exe /k "C:\LVCaixa\venvlvcaixa\Scripts\activate.bat"',SW_SHOW);
WinExec('cmd.exe /k "C:\LVCaixa\venvlvcaixa\Scripts\activate.bat"',SW_HIDE);
end;

procedure TForm2.Button2Click(Sender: TObject);
begin
JvCreateProcess1.Run;
end;

end.
