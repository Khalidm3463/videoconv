import React from 'react'

interface Props {
  srtFile: string
  videoFile?: string
}

const DownloadOptions: React.FC<Props> = ({ srtFile, videoFile }) => {
  return (
    <div className="mt-4 flex flex-col gap-2">
      <a href={srtFile} download className="bg-blue-500 text-white px-4 py-2 rounded shadow hover:bg-blue-600">
        Download SRT
      </a>
      {videoFile && (
        <a href={videoFile} download className="bg-green-500 text-white px-4 py-2 rounded shadow hover:bg-green-600">
          Download Subtitled Video
        </a>
      )}
    </div>
  )
}

export default DownloadOptions
