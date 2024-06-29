program ConsoleExample;
uses
  Forms,
  ConsoleExampleMainFormU in 'C:\Componentes_delphi_10_rio\jvcl-master\jvcl\examples\JvCreateProcess\ConsoleExampleMainFormU.pas' {ConsoleExampleMainForm};

{$R *.res}
begin
  Application.Initialize;
  Application.CreateForm(TConsoleExampleMainForm, ConsoleExampleMainForm);
  application.Run;
end.
