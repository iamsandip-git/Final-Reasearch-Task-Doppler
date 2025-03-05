import React from 'react'


const NewsShow = ({ data, isLoading, isError, error }) => {


  if (isLoading) {
    return <div>
      <h1 className='text-2xl font-bold p-5'>Loading ...</h1>
    </div>
  }


  return (
    <div>
      <h1 className="text-2xl font-bold p-5">News From Across the Web</h1>
      <div className="grid grid-cols-4 gap-3 sm:grid-cols-1 md:grid-cols-1 p-5">


        {(data?.results || []).map((news) => {
          return (
            <div key={news.id} className='w-[300px] md:w-[100%] sm:w-[100%] rounded-md cursor-pointer hover:scale-105 transition-all delay-75 shadow-lg' onClick={() => window.open(news.link, '_blank', 'noopener,noreferrer')}>
              {news.image_url != null ?
                <img src={`${news.image_url}`} className='h-[300px] w-[300px] sm:h-[150px] sm:w-[100px] md:h-[150px] md:w-[100px] rounded-md' alt="" /> : <img src="noimage.jpg" className='h-[300px] w-[300px] sm:h-[150px] sm:w-[100px] md:h-[150px] md:w-[100px] rounded-md' alt="" />
              }
              <div className='p-3 space-y-2'>
                <h1 className='text-xl font-bold'>{news.title}</h1>
              </div>


            </div>
          )
        })}




      </div>
    </div>
  )
}


export default NewsShow