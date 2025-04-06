import React from 'react'
import { useLocation, Link } from 'react-router-dom'
import DownloadOptions from '../components/DownloadOptions'

const Result = () => {
  const { state } = useLocation()
  const { srt_file, video_file } = state || {}

  return (
    <div className="max-w-2xl mx-auto mt-10 px-4">
      <h2 className="text-2xl font-bold mb-4">✅ Subtitles Ready</h2>
      <DownloadOptions srtFile={srt_file} videoFile={video_file} />
      <Link to="/" className="mt-6 inline-block text-blue-500 hover:underline">⬅️ Back to Home</Link>
    </div>
  )
}

export default Result
