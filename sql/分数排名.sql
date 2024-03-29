-- 编写一个 SQL 查询来实现分数排名。如果两个分数相同，则两个分数排名（Rank）相同。请注意，平分后的下一个名次应该是下一个连续的整数值。换句话说，名次之间不应该有“间隔”。

-- +----+-------+
-- | Id | Score |
-- +----+-------+
-- | 1  | 3.50  |
-- | 2  | 3.65  |
-- | 3  | 4.00  |
-- | 4  | 3.85  |
-- | 5  | 4.00  |
-- | 6  | 3.65  |
-- +----+-------+
-- 例如，根据上述给定的 Scores 表，你的查询应该返回（按分数从高到低排列）：

-- +-------+------+
-- | Score | Rank |
-- +-------+------+
-- | 4.00  | 1    |
-- | 4.00  | 1    |
-- | 3.85  | 2    |
-- | 3.65  | 3    |
-- | 3.65  | 3    |
-- | 3.50  | 4    |
-- +-------+------+

-- 来源：力扣（LeetCode）
-- 链接：https://leetcode-cn.com/problems/rank-scores
-- 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




select Score,  
CONVERT((case
when @preScore=Score then @curRank
when @preScore:=Score then @curRank:=@curRank+1
else @curRank:=@curRank+1
end
), SIGNED) as Rank
from Scores, (select @curRank:=0, @preScore:=null) as p
order by Score desc;




select a.Score as Score,  
(select count(distinct b.Score) from Scores as b where b.Score >= a.Score) as 'Rank'
from Scores as a
order by a.Score desc;

select 
    a.Score as Score,
    count(distinct b.Score) as 'Rank'
from Scores as a join Scores as b on a.Score <= b.Score
group by a.id, a.Score
order by a.Score desc;
