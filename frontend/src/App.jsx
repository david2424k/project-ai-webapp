import React from 'react'
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import Projects from './pages/Projects'

export default function App(){
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-gray-50">
        <header className="p-4 bg-white shadow">
          <div className="container mx-auto flex justify-between">
            <Link to="/" className="font-bold">ProjectAI</Link>
            <nav className="space-x-4">
              <Link to="/projects">Проекты</Link>
            </nav>
          </div>
        </header>
        <main className="container mx-auto p-4">
          <Routes>
            <Route path="/" element={<Dashboard/>} />
            <Route path="/projects" element={<Projects/>} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  )
}
