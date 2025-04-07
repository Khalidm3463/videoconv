import React, { useState } from 'react'
import LanguageSelector from './LanguageSelector'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

const UploadForm = () => {
  const [file, setFile] = useState<File | null>(null)
  const [url, setUrl] = useState('')
  const [language, setLanguage] = useState('en')
  const [burn, setBurn] = useState(true)
  const navigate = useNavigate()

  const handleUpload = async () => {
    if (!file) return alert('Select a video file')

    const form = new FormData()
    form.append('file', file)
    form.append('target_lang', language)
    form.append('burn_subs', String(burn))

    const res = await axios.post('/api/process_upload/', form)
    navigate('/result', { state: res.data })
  }

  const handleURL = async () => {
    if (!url) return alert('Enter a valid video URL')

    const form = new FormData()
    form.append('url', url)
    form.append('target_lang', language)
    form.append('burn_subs', String(burn))

    const res = await axios.post('/api/process_link', form)
    navigate('/result', { state: res.data })
  }

  return (
    <div className="space-y-4">
      <div>
        <label className="block mb-1 font-medium">Upload Video</label>
        <input type="file" accept="video/mp4" onChange={(e) => setFile(e.target.files?.[0] || null)} />
        <button onClick={handleUpload} className="ml-2 bg-blue-500 text-white px-3 py-1 rounded">
          Upload
        </button>
      </div>

      <div>
        <label className="block mb-1 font-medium">Or Paste Video URL</label>
        <input
          type="text"
          className="border px-3 py-2 rounded w-2/3"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="YouTube, Twitter, Instagram"
        />
        <button onClick={handleURL} className="ml-2 bg-purple-500 text-white px-3 py-1 rounded">
          Process URL
        </button>
      </div>

      <div className="flex items-center gap-4">
        <label className="font-medium">Subtitle Language:</label>
        <LanguageSelector selected={language} onChange={setLanguage} />
      </div>

      <div className="flex items-center gap-2">
        <input type="checkbox" checked={burn} onChange={(e) => setBurn(e.target.checked)} />
        <label>Bake subtitles into video</label>
      </div>
    </div>
  )
}

export default UploadForm
