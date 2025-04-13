# 🔍 Tactara Deep Research Agent

**Web research, redefined with Agents SDK + Firecrawl.**

Tactara’s Deep Research Agent is a powerful AI tool that performs multi-step, context-rich research using OpenAI’s Agents SDK and Firecrawl’s deep crawl capabilities. From academic reports to business trends, generate expert-level research with just a prompt.

---

## 🚀 Why Teams Choose Tactara

### 🌐 Comprehensive Web Research
- Automatically scrapes the web using [Firecrawl](https://firecrawl.dev)  
- Surfaces high-quality, structured content across sources  
- Iterative search flow for deeper coverage of any topic  

### 🤖 Dual-Agent Research Flow
- **Research Agent**: Collects and synthesizes findings from trusted sources  
- **Elaboration Agent**: Adds contextual depth, examples, and insights using OpenAI’s SDK  
- Multi-phase logic: `search → draft → refine`  

### 🧑‍💻 Streamlit UI for Interactive Use
- Sidebar for API key management  
- Markdown download of final reports  
- Intuitive, click-to-run experience  

---

## 🛠️ Quickstart

### 1. Clone the Repo

```bash
git clone https://github.com/Tactara/deep-research-agent.git
cd deep-research-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Set Your API Keys

You'll need credentials from:

- [OpenAI](https://platform.openai.com)  
- [Firecrawl](https://firecrawl.dev)

Input them via the Streamlit sidebar on first run.

---

### 4. Launch the App

```bash
streamlit run deep_research_agent.py
```

---

## 🧠 How It Works

| Phase            | Description                                             |
|------------------|---------------------------------------------------------|
| 📝 **Input**      | User enters a topic or question                         |
| 🔍 **Research**   | Firecrawl performs deep search and content extraction   |
| 📄 **Draft Report** | Initial synthesis is created using OpenAI               |
| 🧾 **Enhance**    | Elaboration agent adds clarity, detail, and structure   |
| 💾 **Output**     | User downloads markdown-formatted final report          |

---

## 🧪 Example Prompts

- "Latest developments in quantum computing"  
- "How generative AI is transforming supply chains"  
- "Comparative analysis: EV adoption in Europe vs. Asia"  
- "Ethical frameworks for autonomous drones"  

---

## 🧩 Ideal For

- Strategy teams needing fast, AI-driven landscape research  
- Consultants preparing deep-dive reports for clients  
- Founders, PMs, and VCs exploring emerging trends  
- Students or researchers needing synthesis across sources  

---

**Built with ❤️ by [Tactara.ai](https://www.tactara.ai)**