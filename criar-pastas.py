import os

# modulos a serem criados
ferramentas_path = "Ferramentas - XT"
gestao_path = "Gestão Empresarial - ERP XT"

# lista de nome de trilhas em Ferramentas - XT 
ferramentas_folders = [
    "LSP - Básico",
    "LSP - Intermediário",
    "LSP - Avançado",
    "Regras LSP - Controle de Ponto",
    "Regras LSP - Administração de Pessoal",
    "CBDS",
    "Gerador de Relatórios Gestão de Pessoas - Básico",
    "Gerador de Relatórios Gestão de Pessoas - Intermediário",
    "Gerador de Relatórios Gestão de Pessoas - Avançado",
    "Gerador de Relatórios Gestão Empresarial _ ERP - Básico",
    "Gerador de Relatórios Gestão Empresarial _ ERP - Intermediário",
    "Gerador de Relatorios Gestão Empresarial _ ERP - Avançado",
    "Gerador de Cubos",
    "Gerador de Importação e Exportação",
    "Gerenciador de Usuários (SGU)",
    "Gerador de Telas (SGI)",
    "eDocs - Instalação e Atualização de Versão",
    "Atualização dos Produtos Senior (Tecnologias G5 G6)",
    "Instalação dos Produtos Senior (Tecnologias G5 G6)",
    "Web Service na G5",
    "Processos Automáticos (Tecnologias G5 G6)"
]

# lista de nome de trilhas em Gestão Empresarial _ ERP XT
gestao_folders = [
    "Boas-vindas à Trilha Gestão Empresarial _ ERP XT",
    "ERP XT Cadastros Iniciais",
    "ERP XT Suprimentos",
    "ERP XT Mercado",
    "ERP XT Finanças",
    "ERP XT Controladoria",
    "ERP XT Manufatura",
    "ERP XT Custos",
    "ERP XT Serviços",
    "ERP XT Qualidade",
    "eDocs - Integração ERP XT",
    "ERP XT Integrações",
    "ERP XT Agronegócio",
    "ERP XT Customização",
    "ERP XT Instalação",
    "SUPORTE ERP RESPONDE"
]

# criar pasta de ferramentas
for ferramenta_folder in ferramentas_folders:
    path = os.path.join(ferramentas_path, ferramenta_folder)
    try:
        os.makedirs(path, exist_ok=True)
        print(f"✅ [ferramentas] criado pasta: {path}")
    except Exception as e:
        print(f"❌ [ferramentas] erro ao criar pasta {path}: {e}")


# criar pasta de gestão
for gestao_folder in gestao_folders:
    path = os.path.join(gestao_path, gestao_folder)
    try:
        os.makedirs(path, exist_ok=True)
        print(f"✅ [gestao-empresarial] criado pasta: {path}")
    except Exception as e:
        print(f"❌ [gestao-empresarial] erro ao criar pasta {path}: {e}")

