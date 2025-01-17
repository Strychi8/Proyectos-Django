import { useNavigate } from 'react-router-dom'

export function TaskCard({ tasks }) {

    const navigate = useNavigate()

    return (
        <div className="bg-zinc-800 p-3 hover:bg-zinc-700 hover:cursor-pointer"

            onClick={() => {
                navigate(`/tasks/${tasks.id}`)
            }}
        >
            <h1 className='font-bold uppercase'>{tasks.title}</h1>
            <p className='text-slate-400'>{tasks.description}</p>
        </div>
    )
}