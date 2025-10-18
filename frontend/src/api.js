const API = import.meta.env.VITE_API_URL || 'http://localhost:8000'
export async function fetchProjects(){
  const r = await fetch(`${API}/projects`)
  return r.json()
}
export async function createProject(payload){
  const r = await fetch(`${API}/projects`, {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)})
  return r.json()
}
export async function aiRecommend(payload){
  const r = await fetch(`${API}/ai/recommend`, {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)})
  return r.json()
}
