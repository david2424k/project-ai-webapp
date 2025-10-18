import React, {useEffect, useState} from 'react'
import { fetchProjects, createProject, aiRecommend } from '../api'

export default function Projects(){
  const [projects, setProjects] = useState([])
  const [name, setName] = useState('')

  useEffect(()=>{ fetchProjects().then(setProjects) }, [])

  async function handleCreate(){
    const p = await createProject({name, description:''})
    setProjects(prev=>[...prev,p])
    setName('')
  }

  async function handleRecommend(){
    const rec = await aiRecommend({project_id: projects[0]?.id || 0, task_title:'Демо', task_description:'Описание задачи'})
    alert(JSON.stringify(rec))
  }

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Проекты</h1>
      <div className="mb-4 flex gap-2">
        <input value={name} onChange={e=>setName(e.target.value)} className="border p-2" placeholder="Название проекта" />
        <button onClick={handleCreate} className="bg-blue-600 text-white px-4 py-2 rounded">Создать</button>
        <button onClick={handleRecommend} className="bg-green-600 text-white px-4 py-2 rounded">Получить рекомендацию ИИ</button>
      </div>
      <div className="grid grid-cols-3 gap-4">
        {projects.map(p => (
          <div key={p.id} className="p-4 bg-white rounded shadow">
            <h3 className="font-semibold">{p.name}</h3>
            <p className="text-sm text-gray-500">{p.description}</p>
          </div>
        ))}
      </div>
    </div>
  )
}
