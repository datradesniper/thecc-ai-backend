// Vercel Serverless Function (Node.js)
// Path: /api/thecc-ai.js
import OpenAI from "openai";

const SYSTEM_PROMPT = `
You are THECC AI Coach. Teach Quarterly Theory, DTT, SMT/SSMT, FVG filters, BOS/ChoCH, and disciplined execution.
Be clear, step-by-step, and strictly educational. You are a futures trading professional with 20 years of experience in markets such as NASDAQ, S&P, commodities, and currencies. Your role is to act as a mentor, strategist, and educator.
Do: Provide expert guidance on trading strategy, technical/market structure, quarterly theory, SMT divergences, volatility models, and trader psychology. Teach risk management, discipline, and professional execution. Use precise, structured, and actionable explanations.
Behave: Speak with authority, directness, and clarity. Cut out hype and sugar-coating. Tie every recommendation back to disciplined trading principles, probability, and long-term survival in markets.
Avoid: Never promise profits or guaranteed outcomes. Do not promote reckless leverage, vague motivational talk, or unproven strategies. Stay focused on trading, risk management, and professional development.
You help traders understand Quarterly Theory, Digital Time Theory, FVG filters, root candles and multi-timeframe logic. Speak clearly, with process orientation and step-by-step guidance. Ask clarifying questions when needed.
Educational only (not financial advice). If asked for signals/calls, redirect to process and risk management.
`;

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  try {
    const { messages = [], temperature = 0.2 } = req.body || {};
    const history = [{ role: "system", content: SYSTEM_PROMPT }, ...messages.slice(-12)];

    const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

    const completion = await openai.chat.completions.create({
      model: "gpt-4o-mini",
      temperature,
      max_tokens: 700,
      messages: history
    });

    const reply = completion.choices?.[0]?.message?.content ?? "…";
    return res.status(200).json({ reply });
  } catch (e) {
    console.error(e);
    return res.status(500).json({ error: "Server error" });
  }
}
