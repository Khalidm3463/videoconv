import React from 'react'
import UploadForm from '../components/UploadForm'

const Home = () => {
  return (
    <div className="max-w-2xl mx-auto mt-10 px-4">
      <h1 className="text-3xl font-bold mb-6">🎬 AI Video Subtitle Translator</h1>
      <UploadForm />
    </div>
  )
}

export default Home
