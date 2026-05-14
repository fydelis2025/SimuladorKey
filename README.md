# ⌨️ SimuladorKey

O **SimuladorKey** é uma ferramenta de automação desenvolvida para emular entradas de teclado de forma programática. Projetado com foco em precisão e baixo nível, o simulador permite a automação de sequências de digitação, comandos complexos e testes de interface diretamente no sistema operacional.

---

## 🔍 Sobre o Projeto

Este projeto nasceu da necessidade de automatizar tarefas repetitivas e validar a entrada de dados em ambientes controlados. Ele utiliza chamadas de sistema para injetar eventos de teclado na fila de mensagens do hardware, garantindo que o sistema reconheça a entrada como se fosse uma ação humana real.

### Principais Aplicações:
*   **Automação de SysAdmin:** Configuração rápida de servidores e scripts pós-instalação.
*   **QA & Testes:** Validação de fluxos de entrada em aplicações que não possuem APIs de teste.
*   **Pesquisa de Segurança:** Estudo de vetores de ataque via injeção de caracteres (HID emulation).

## 🚀 Funcionalidades

*   ✅ **Injeção de Texto Real:** Suporte a caracteres alfanuméricos e símbolos.
*   ✅ **Comandos de Sistema:** Emulação de teclas como `ENTER`, `TAB`, `CTRL`, `ALT` e `ESC`.
*   ✅ **Timing Customizável:** Configuração de intervalos (delay) entre as teclas para evitar bloqueios de buffer.
*   ✅ **Leve e Portátil:** Executável minimalista com poucas dependências.

## 🛠️ Tecnologias e Requisitos

*   **Linguagem:** [Adicione aqui, ex: C# / C++ / Python]
*   **Compatibilidade:** Windows (via User32.dll) / [Linux se aplicável].
*   **Target:** Sistemas x64/x86.

## 📥 Como Utilizar

1. **Clonagem:**
   ```bash
   git clone [https://github.com/fydelis2025/SimuladorKey.git](https://github.com/fydelis2025/SimuladorKey.git)
