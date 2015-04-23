%"path_before% @echo off
%"path_vs2010% set filename=%VS100COMNTOOLS%vsvars32.bat
%"path_after%  if not exist "%filename%" goto eof
%"path_after%  call "%filename%"
%"path_after%  call path.bat
%"path_after%  devenv ALVAR.sln
