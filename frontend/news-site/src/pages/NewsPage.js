import React, { useEffect, useState } from 'react'
import { fetchAllNews } from '../features/newsApi'
import NewsShow from '../components/NewsShow'

const NewsPage = () => {
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(null);
  const [data, setData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isError, setIsError] = useState(false);

  useEffect(() => {
    const getNews = async () => {
      setIsLoading(true);
      setIsError(false);
      try {

        const newsData = await fetchAllNews(page);
        setData(newsData);


        if (newsData?.count) {
          const pages = Math.ceil(newsData.count / 24);
          setTotalPages(pages);
        }

      } catch (error) {
        setIsError(true);
      } finally {
        setIsLoading(false);
      }

    };
    getNews();
  }, [page]);


  const handlePrevious = () => setPage((prevPage) => Math.max(prevPage - 1, 1));
  const handleNext = () => setPage((prevPage) => prevPage + 1);
  const handleFirst = () => setPage(1);
  const handleLast = () => setPage(totalPages);


  return (
    <div>
      <header className='bg-[#032541] text-white flex justify-between px-4 py-2 items-center pt-5'>
        <h1 className='text-4xl font-bold mb-2 mr-5'>News-Aggregator</h1>
      </header>
      <NewsShow data={data} isLoading={isLoading} isError={isError} error={null} />

      <div className='flex justify-center gap-5'>

        {data?.previous && (<button className="py-2 px-4 bg-blue-500 text-white hover:bg-blue-600 focus:outline-none" onClick={handleFirst} disabled={!data?.previous}>
          First
        </button>)}

        {data?.previous && (<button className="py-2 px-4 bg-blue-500 text-white hover:bg-blue-600 focus:outline-none" onClick={handlePrevious} disabled={!data?.previous}>
          Previous
        </button>)}

        <span className="py-2 px-4">Page {page}</span>
        {data?.next && (
          <button className="py-2 px-4 bg-blue-500 text-white hover:bg-blue-600 focus:outline-none" onClick={handleNext}>
            Next
          </button>
        )}

        {totalPages && page !== totalPages && (
          <button
            className="py-2 px-4 bg-blue-500 text-white hover:bg-blue-600 focus:outline-none"
            onClick={handleLast}
          >
            Last
          </button>
        )}

      </div>
    </div>
  )
}

export default NewsPage