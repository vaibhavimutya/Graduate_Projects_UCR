package edu.ucr.ir.IRSearchEngine.controller;

import edu.ucr.ir.IRSearchEngine.model.SearchResultEntity;
import edu.ucr.ir.IRSearchEngine.service.LuceneSearchService;
import org.apache.lucene.queryparser.classic.ParseException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;




import java.io.IOException;
import java.util.List;


@RestController
@RequestMapping("api/getSearchResults")
public class SearchController {
    private final LuceneSearchService luceneSearchService;
    @Autowired
    public SearchController(LuceneSearchService luceneSearchService) {
        this.luceneSearchService = luceneSearchService;
    }
    @GetMapping("/LuceneSearch/{searchTerm}")
    public List<SearchResultEntity> getLuceneSearch(@PathVariable(value = "searchTerm") String searchTerm) throws IOException, ParseException {
        return luceneSearchService.getSearchResults(searchTerm);
    }

//    @GetMapping("/HadoopSearch/{searchTerm}")
//    public List<SearchResult> placeOrder() throws IOException {
//        return
//    }


}

