@echo off
echo Criando estrutura de pastas e arquivos...

:: Criar Pastas
mkdir static
mkdir templates

:: Criar Arquivos
type nul > templates\index.html
type nul > .gitignore
type nul > app.py
type nul > dados.json
type nul > package.json
type nul > requirements.txt
type nul > vercel.json

echo Estrutura criada com sucesso!
pause